<script lang="ts">
  import { Canvas } from '@threlte/core';
  import { OrbitControls } from '@threlte/extras'; // Keep OrbitControls from extras
  import { useGLTF } from '@threlte/gltf'; // Import useGLTF from gltf
  import { DirectionalLight, AmbientLight } from 'three';

  // Load the GLB model
  // The path is relative to the `static` directory
  const gltf = useGLTF('/models/garden.glb');
</script>

<div style="height: 100vh; width: 100vw; position: absolute; top: 0; left: 0;">
  <Canvas>
    <DirectionalLight position={[3, 3, 3]} />
    <AmbientLight intensity={0.5} />

    {#if $gltf}
      <primitive object={$gltf.scene} />
    {/if}

    <OrbitControls />
  </Canvas>
</div>