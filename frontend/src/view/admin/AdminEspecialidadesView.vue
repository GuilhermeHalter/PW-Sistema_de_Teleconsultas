<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />
    
    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold text-dark mb-1">Gerenciar Especialidades</h3>
          <p class="text-muted">Cadastre, edite e remova as especialidades médicas do sistema</p>
        </div>
        <button class="btn btn-danger px-4 py-2 rounded-3 fw-bold d-flex align-items-center gap-2" @click="abrirModal()">
          <i class="bi bi-plus-lg"></i> Nova Especialidade
        </button>
      </header>

      <div v-if="error" class="alert alert-danger py-2 small mb-3">{{ error }}</div>

      <div v-if="loading" class="text-center py-5">
        <div class="spinner-border text-danger"></div>
      </div>

      <div v-else class="section-card overflow-hidden">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th class="px-4 py-3" style="width: 100px;">ID</th>
              <th>Nombre</th>
              <th>Descripción</th>
              <th class="text-end px-4" style="width: 150px;">Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="especialidades.length === 0">
              <td colspan="4" class="text-center py-4 text-muted">Ninguna especialidad encontrada</td>
            </tr>
            <tr v-for="esp in especialidades" :key="esp.id">
              <td class="px-4 py-3 font-monospace small text-muted">#{{ esp.id }}</td>
              <td>
                <span class="fw-semibold text-dark">{{ esp.nombre }}</span>
              </td>
              <td class="small text-muted">{{ esp.descripcion || '—' }}</td>
              <td class="text-end px-4">
                <button class="btn btn-sm btn-outline-secondary rounded-3 me-1 px-3" @click="abrirModal(esp)">
                  <i class="bi bi-pencil"></i>
                </button>
                <button class="btn btn-sm btn-outline-danger rounded-3 px-3" @click="remove(esp)">
                  <i class="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="modalAberto" class="modal-overlay d-flex align-items-center justify-content-center" @click.self="fecharModal">
        <div class="modal-card p-4">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h5 class="fw-bold mb-0">{{ editing ? 'Editar Especialidad' : 'Nueva Especialidad' }}</h5>
            <button class="btn btn-sm btn-outline-secondary rounded-circle" @click="fecharModal">
              <i class="bi bi-x"></i>
            </button>
          </div>

          <div class="row g-3">
            <div class="col-12">
              <label class="form-label">Nombre *</label>
              <input v-model="form.nombre" class="form-control rounded-3" placeholder="Ex: Cardiologia" required />
            </div>
            <div class="col-12">
              <label class="form-label">Descripción</label>
              <textarea v-model="form.descripcion" class="form-control rounded-3" placeholder="Breve descripción de la especialidad" rows="3"></textarea>
            </div>
          </div>

          <div class="d-flex gap-2 mt-4">
            <button class="btn btn-danger flex-grow-1 rounded-3 fw-bold" @click="onSubmit" :disabled="salvando">
              <span v-if="salvando" class="spinner-border spinner-border-sm me-2"></span>
              {{ salvando ? 'Guardando...' : (editing ? 'Salvar Alterações' : 'Cadastrar Especialidad') }}
            </button>
            <button class="btn btn-outline-secondary rounded-3 px-4" @click="fecharModal">Cancelar</button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import SidebarAdminComp from '../../components/admin/SidebarAdminComp.vue'
import api from '../../services/api' // Mantido o seu import original de serviço

const especialidades = ref([])
const loading = ref(false)
const salvando = ref(false)
const error = ref(null)
const modalAberto = ref(false)
const editing = ref(false)

const form = reactive({ id: null, nombre: '', descripcion: '' })
const apiBase = '/api/especialidades'

// Buscar dados da API
async function fetchAll() {
  loading.value = true
  error.value = null
  try {
    // Caso sua API retorne os dados dentro de .data como no script dos médicos, 
    // altere para: const res = await api.get(apiBase); especialidades.value = res.data
    especialidades.value = await api.get(apiBase)
  } catch (err) {
    error.value = err.message || 'Error al cargar especialidades.'
  } finally {
    loading.value = false
  }
}

// Controladores do Modal
function abrirModal(esp = null) {
  error.value = null
  if (esp) {
    editing.value = true
    form.id = esp.id
    form.nombre = esp.nombre
    form.descripcion = esp.descripcion
  } else {
    editing.value = false
    resetForm()
  }
  modalAberto.value = true
}

function fecharModal() {
  modalAberto.value = false
  resetForm()
}

function resetForm() {
  form.id = null
  form.nombre = ''
  form.descripcion = ''
}

// Criar ou Atualizar Registro
async function onSubmit() {
  if (!form.nombre.trim()) {
    error.value = 'El campo Nombre es obligatorio.'
    return
  }
  
  salvando.value = true
  error.value = null
  try {
    const payload = { nombre: form.nombre, descripcion: form.descripcion }
    if (editing.value) {
      await api.put(`${apiBase}/${form.id}`, payload)
    } else {
      await api.post(apiBase, payload)
    }
    fecharModal()
    await fetchAll()
  } catch (err) {
    error.value = err.message || 'Error al guardar la especialidad.'
  } finally {
    salvando.value = false
  }
}

// Remover Registro
async function remove(esp) {
  if (!confirm(`¿Eliminar especialidad "${esp.nombre}"? Esta acción es irreversible.`)) return
  try {
    await api.delete(`${apiBase}/${esp.id}`)
    await fetchAll()
  } catch (err) {
    error.value = err.message || 'Error al eliminar la especialidad.'
  }
}

onMounted(fetchAll)
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper { background-color: #fff5f5; min-height: 100vh; }
.section-card { background: white; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.form-label { font-size: 0.85rem; font-weight: 600; color: #1e293b; margin-bottom: 0.3rem; display: block; }
.form-control { border: 1.5px solid #e2e8f0; padding: 10px 14px; }
.form-control:focus { border-color: #dc2626; box-shadow: 0 0 0 3px rgba(220,38,38,0.1); }
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 1000; backdrop-filter: blur(2px); }
.modal-card { background: white; border-radius: 20px; width: 100%; max-width: 540px; box-shadow: 0 20px 60px rgba(0,0,0,0.2); max-height: 90vh; overflow-y: auto; }
</style>