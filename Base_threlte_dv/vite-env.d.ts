// vite-env.d.ts
declare module '*.gltf' {
    const src: string;
    export default src;
}

declare module '*.glb' {
    const src: string;
    export default src;
}

