# Frontend: Vue and TypeScript

- Use Vue 3, Composition API, script setup and strict TypeScript checking.
- Keep one Vue component per .vue file. Each component owns a cohesive part of the interface; do not split simple markup mechanically.
- Do not use any to bypass typing problems. Document justified exceptions.
- Put HTTP calls in a typed API module. Do not scatter fetch calls and URLs across components.
- Client validation improves user experience; server validation remains mandatory.
- Explicitly handle loading, success, error and empty-gallery states.
- Do not display successful upload or deletion before the server confirms it.
- Release object URLs used for local previews when they are no longer needed.
- Provide accessible buttons and fields, keyboard navigation for the photo viewer and a responsive layout.
- Extract shared logic into composables only when there is a clear common responsibility.
- Run vue-tsc separately from the Vite build.
- Use ESLint, Prettier, component behavior tests and end-to-end scenarios.
- Prefer relative API URLs. Use a development proxy and a single application origin in Compose.
