import { NavLink } from 'react-router'

const navItems = [
  { path: '/', label: 'Home' },
  { path: '/dashboard', label: 'Dashboard' },
  { path: '/user', label: 'User' },
  { path: '/login', label: 'Login' },
]

export function Sidebar() {
  return (
    <aside className="hidden w-56 border-r border-slate-200 bg-white p-4 md:block">
      <nav className="flex flex-col gap-2">
        {navItems.map((item) => (
          <NavLink
            className={({ isActive }) =>
              [
                'rounded-md px-3 py-2 text-sm font-medium',
                isActive ? 'bg-blue-50 text-blue-700' : 'text-slate-600',
              ].join(' ')
            }
            key={item.path}
            to={item.path}
          >
            {item.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}
