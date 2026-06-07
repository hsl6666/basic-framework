import type { AxiosRequestConfig } from 'axios'

export type HttpMethod = 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE'

export interface RequestOptions<TBody = unknown>
  extends Omit<AxiosRequestConfig<TBody>, 'data' | 'method' | 'url'> {
  method?: HttpMethod
  body?: TBody
}

export interface ApiResponse<TData> {
  code: number
  message: string
  data: TData
}
