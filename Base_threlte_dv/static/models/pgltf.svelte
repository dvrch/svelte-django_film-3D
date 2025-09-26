<script lang="ts">
    import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
    import { T } from '@threlte/core';
    import { OrbitControls } from '@threlte/extras';
    import * as THREE from 'three';

    let mesh: any;

    const loader = new GLTFLoader();
    loader.load('bibi.glb', (gltf) => {
        const geometry = (gltf.scene.children[0] as THREE.Mesh).geometry; // Ajout d'une assertion de type
        const texture = new T.TextureLoader().load('bibi.png');
        const material = new T.MeshStandardMaterial({ map: texture, shininess: 1, roughness: 0.5 }); // Ajout d'un argument 'roughness'
        mesh = new T.Mesh(geometry, material);
    }, undefined, (error) => {
        console.error('Erreur lors du chargement du modèle GLTF:', error);
    });
</script>

<T.PerspectiveCamera makeDefault position={[0, 1.5, 4]} fov={70}>
    <OrbitControls autoRotate enableZoom={true} minDistance={8} maxDistance={80} target={[0, 1.5, 0]} />
</T.PerspectiveCamera>

<T.DirectionalLight intensity={0.8} position={[0, 4, 4]} />

{#if mesh}
    <T.Mesh {mesh} />
{/if}



<!-- 

import * as THREE from 'three'
import GLTFLoader from 'gltfloader'
 
const scene = new THREE.Scene()

const camera = new THREE.PerspectiveCamera(70, iw / ih)

const geometry = await GLTFLoader.loadGeometry('bibi.glb')

const texture = await GLTFLoader.loadTexture('bibi.png')
const material = new THREE.MeshPhongMaterial({ map:texture,shininess:1 })

const mesh = new THREE.Mesh(geometry, material)

const light = new THREE.PointLight(0xffffff)

scene.add(light)
scene.add(mesh)

camera.position.set(0, 1.5, 4)
light.position.set(0, 4, 4)

const renderer = new THREE.WebGLRenderer({ canvas })

let t = 0
const clock = new THREE.Clock();

loop()

function loop() {
  t += clock.getDelta()
  mesh.morphTargetInfluences[1] = Math.abs(Math.cos(t))
  mesh.rotation.y = Math.cos(t/2)
  renderer.render(scene, camera)
  requestAnimationFrame(loop)
}


 -->
