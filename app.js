// SDK создаёт Telegram.WebApp и в обычном браузере, поэтому «внутри Telegram»
// определяем по платформе, а не по наличию объекта.
(() => {
  const tg = window.Telegram && window.Telegram.WebApp;
  const inTg = !!tg && tg.platform && tg.platform !== 'unknown';

  if (!inTg) {
    // в браузере сайты открываем рядом, чтобы хаб не терялся
    document.querySelectorAll('.work[data-kind="site"]').forEach((a) => {
      a.target = '_blank';
      a.rel = 'noopener';
    });
    return;
  }

  tg.ready();
  tg.expand();
  try {
    tg.setHeaderColor('secondary_bg_color');
    tg.setBackgroundColor('secondary_bg_color');
  } catch (e) { /* старые клиенты без этих методов — оставляем их цвета */ }

  document.addEventListener('click', (ev) => {
    const a = ev.target.closest('.work');
    if (!a) return;
    ev.preventDefault();
    if (tg.HapticFeedback) tg.HapticFeedback.selectionChanged();
    // Обычный переход по t.me внутри Mini App открыл бы страницу бота в webview,
    // а сайт — внутри хаба без кнопки назад
    if (a.dataset.kind === 'bot') tg.openTelegramLink(a.href);
    else tg.openLink(a.href, { try_instant_view: false });
  });
})();
