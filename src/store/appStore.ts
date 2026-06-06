import { create } from 'zustand'

type AppStatus = 'idle' | 'running'

interface AppState {
  status: AppStatus
  start: () => void
  stop: () => void
  toggle: () => void
}

export const useAppStore = create<AppState>((set) => ({
  status: 'idle',
  start: () => set({ status: 'running' }),
  stop: () => set({ status: 'idle' }),
  toggle: () =>
    set((state) => ({
      status: state.status === 'running' ? 'idle' : 'running',
    })),
}))
