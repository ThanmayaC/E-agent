// Workspace preferences, kept on this device. The backend has no user model
// yet (arrives in V2), so role and theme are client-side switches.

const THEME_KEY = 'edip.theme'
const ADMIN_KEY = 'edip.admin'
const NOTIFY_KEY = 'edip.notify-prefs'

export const getTheme = () => localStorage.getItem(THEME_KEY) || 'midnight'

export function setTheme(theme) {
  localStorage.setItem(THEME_KEY, theme)
  document.documentElement.dataset.theme = theme
}

export const isAdmin = () => localStorage.getItem(ADMIN_KEY) === 'on'

export function setAdmin(on) {
  if (on) localStorage.setItem(ADMIN_KEY, 'on')
  else localStorage.removeItem(ADMIN_KEY)
  window.dispatchEvent(new Event('edip-admin-changed'))
}

const NOTIFY_DEFAULTS = {
  critical_risk: true,
  portfolio_change: true,
  new_report: true,
  recommendation: true,
  task_deadline: true,
  workflow_failure: true,
}

export function getNotifyPrefs() {
  try {
    return { ...NOTIFY_DEFAULTS, ...JSON.parse(localStorage.getItem(NOTIFY_KEY) || '{}') }
  } catch {
    return { ...NOTIFY_DEFAULTS }
  }
}

export function setNotifyPref(kind, enabled) {
  const prefs = getNotifyPrefs()
  prefs[kind] = enabled
  localStorage.setItem(NOTIFY_KEY, JSON.stringify(prefs))
  return prefs
}
