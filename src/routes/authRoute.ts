export const publicRoutes = ['/login']

export function isPublicRoute(pathname: string) {
  return publicRoutes.includes(pathname)
}
