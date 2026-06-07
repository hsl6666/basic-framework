import { useCallback, useEffect, useState } from 'react'

export function useFetch<T>(fetcher: () => Promise<T>, immediate = true) {
  const [data, setData] = useState<T | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<Error | null>(null)

  const run = useCallback(async () => {
    setLoading(true)
    setError(null)

    try {
      const result = await fetcher()
      setData(result)
      return result
    } catch (requestError) {
      const normalizedError =
        requestError instanceof Error ? requestError : new Error('Request failed')
      setError(normalizedError)
      throw normalizedError
    } finally {
      setLoading(false)
    }
  }, [fetcher])

  useEffect(() => {
    if (immediate) {
      void run()
    }
  }, [immediate, run])

  return { data, loading, error, run }
}
