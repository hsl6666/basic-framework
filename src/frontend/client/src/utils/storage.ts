export const storage = {
  get<T>(key: string): Nullable<T> {
    const value = localStorage.getItem(key)
    return value ? (JSON.parse(value) as T) : null
  },
  set<T>(key: string, value: T) {
    localStorage.setItem(key, JSON.stringify(value))
  },
  remove(key: string) {
    localStorage.removeItem(key)
  },
}
