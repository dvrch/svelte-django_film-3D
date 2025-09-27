<script lang="ts">
  import { Canvas } from '@threlte/core';
  import { OrbitControls, useGLTF } from '@threlte/extras';
  import { DirectionalLight, AmbientLight } from 'three';
  import { browser } from '$app/environment'; // Import browser from SvelteKit

  let gltf: any; // Declare gltf outside the if (browser) block

  // Only load the GLB model on the client-side
  if (browser) {
    gltf = useGLTF('/models/garden.glb');
  }
</script>

<div style="height: 100vh; width: 100vw; position: absolute; top: 0; left: 0;">
  <Canvas>
    <DirectionalLight position={[3, 3, 3]} />
    <AmbientLight intensity={0.5} />

    {#if gltf && $gltf} // Check if gltf is defined and then if $gltf has a value
      <primitive object={$gltf.scene} />
    {/if}

    <OrbitControls />
  </Canvas>
</div>