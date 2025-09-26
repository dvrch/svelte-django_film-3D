<script lang="ts">
  import { T, forwardEventHandlers } from '@threlte/core';
  import { useGltf } from '@threlte/extras';

  export let position = { x: 0, y: 0, z: 0 };
  export let rotation = { x: 0, y: 0, z: 0 };

  const gltf = useGltf('static/models/garden1.glb');
  const component = forwardEventHandlers();
</script>

<T.Group position={[position.x, position.y, position.z]} rotation={[rotation.x, rotation.y, rotation.z]} bind:this={$component}>
  {#await gltf}
    <slot name="fallback" />
  {:then gltf}
    {#if gltf.nodes.default} <!-- Vérification ajoutée -->
      <T.Mesh geometry={gltf.nodes.default.geometry} material={gltf.materials.default} />
    {:else}
      <slot name="error" error="Le modèle GLTF est introuvable." /> <!-- Message d'erreur -->
    {/if}
  {:catch error}
    <slot name="error" {error} />
  {/await}
</T.Group>
