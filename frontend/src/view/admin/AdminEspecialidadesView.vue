<template>
  <div class="admin-especialidades">
    <h2>Especialidades</h2>

    <form @submit.prevent="onSubmit" class="form-inline">
      <input v-model="form.nombre" placeholder="Nombre" required />
      <input v-model="form.descripcion" placeholder="Descripción" />
      <button type="submit">{{ editing ? 'Actualizar' : 'Agregar' }}</button>
      <button type="button" v-if="editing" @click="cancelEdit">Cancelar</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="esp in especialidades" :key="esp.id">
          <td>{{ esp.id }}</td>
          <td>{{ esp.nombre }}</td>
          <td>{{ esp.descripcion }}</td>
          <td>
            <button @click="startEdit(esp)">Editar</button>
            <button @click="remove(esp)" class="danger">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <p v-if="loading">Cargando...</p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import api from '../../services/api'

export default {
  name: 'AdminEspecialidadesView',
  setup() {
    const especialidades = ref([])
    const loading = ref(false)
    const error = ref(null)

    const form = ref({ id: null, nombre: '', descripcion: '' })
    const editing = ref(false)

    const apiBase = '/api/especialidades'

    async function fetchAll() {
      loading.value = true
      error.value = null
      try {
        // using shared api service
        especialidades.value = await api.get(apiBase)
      } catch (err) {
        error.value = err.message
      } finally {
        loading.value = false
      }
    }

    async function onSubmit() {
      if (!form.value.nombre) return
      try {
        const payload = { nombre: form.value.nombre, descripcion: form.value.descripcion }
        if (editing.value) {
          await api.put(`${apiBase}/${form.value.id}`, payload)
        } else {
          await api.post(apiBase, payload)
        }
        await fetchAll()
        resetForm()
      } catch (err) {
        error.value = err.message
      }
    }

    function startEdit(esp) {
      form.value = { id: esp.id, nombre: esp.nombre, descripcion: esp.descripcion }
      editing.value = true
    }

    function cancelEdit() {
      resetForm()
    }

    function resetForm() {
      form.value = { id: null, nombre: '', descripcion: '' }
      editing.value = false
    }

    async function remove(esp) {
      if (!confirm(`Eliminar especialidad "${esp.nombre}"?`)) return
      try {
        await api.delete(`${apiBase}/${esp.id}`)
        await fetchAll()
      } catch (err) {
        error.value = err.message
      }
    }

    onMounted(fetchAll)

    return { especialidades, loading, error, form, editing, onSubmit, startEdit, cancelEdit, remove }
  }
}
</script>

<style scoped>
.admin-especialidades { max-width: 900px; margin: 16px auto; }
table { width: 100%; border-collapse: collapse; margin-top: 12px }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left }
.form-inline { display: flex; gap: 8px; align-items: center }
.form-inline input { padding: 6px }
.danger { background: #e74c3c; color: white; }
.error { color: #c0392b }
</style>
