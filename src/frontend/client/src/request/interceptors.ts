import type {
  AxiosError,
  AxiosInstance,
  InternalAxiosRequestConfig,
} from 'axios'

export function setupInterceptors(instance: AxiosInstance) {
  instance.interceptors.request.use(
    (config: InternalAxiosRequestConfig) => {
      return config
    },
    (error: AxiosError) => Promise.reject(error),
  )

  instance.interceptors.response.use(
    (response) => response.data,
    (error: AxiosError) => Promise.reject(error),
  )
}
