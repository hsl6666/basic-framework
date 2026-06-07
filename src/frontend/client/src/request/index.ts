import axios from 'axios'
import { setupInterceptors } from './interceptors'
import type { RequestOptions } from './types'

export const http = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 10000,
})

setupInterceptors(http)

export async function request<TData, TBody = unknown>(
  url: string,
  options: RequestOptions<TBody> = {},
): Promise<TData> {
  return http.request<TData, TData, TBody>({
    ...options,
    url,
    method: options.method ?? 'GET',
    data: options.body,
  })
}
