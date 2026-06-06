export function isEmail(value: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)
}

export function isRequired(value: unknown) {
  return value !== undefined && value !== null && value !== ''
}
