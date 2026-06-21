<template>
  <div class="d-flex dashboard-wrapper">
    <SidebarAdminComp />

    <main class="content flex-grow-1 p-4">
      <header class="d-flex justify-content-between align-items-center mb-4">
        <div>
          <h3 class="fw-bold text-dark mb-1">Gerenciar Especialidades</h3>
          <p class="text-muted">
            Cadastre, edite e remova as especialidades médicas do sistema
          </p>
        </div>

        <button
          class="btn btn-danger px-4 py-2 rounded-3 fw-bold d-flex align-items-center gap-2"
          @click="abrirModal()"
        >
          <i class="bi bi-plus-lg"></i>
          Nova Especialidade
        </button>
      </header>

      <div v-if="erro" class="alert alert-danger py-2 small mb-3">
        {{ erro }}
      </div>

      <div v-if="carregando" class="text-center py-5">
        <div class="spinner-border text-danger"></div>
      </div>

      <div v-else class="section-card overflow-hidden">
        <table class="table table-hover mb-0">
          <thead class="table-light">
            <tr>
              <th class="px-4 py-3" style="width: 100px">ID</th>
              <th>Nome</th>
              <th>Descrição</th>
              <th class="text-end px-4" style="width: 150px">Ações</th>
            </tr>
          </thead>

          <tbody>
            <tr v-if="especialidades.length === 0">
              <td colspan="4" class="text-center py-4 text-muted">
                Nenhuma especialidade encontrada
              </td>
            </tr>

            <tr
              v-for="especialidade in especialidades"
              :key="especialidade.id"
            >
              <td class="px-4 py-3 font-monospace small text-muted">
                #{{ especialidade.id }}
              </td>

              <td>
                <span class="fw-semibold text-dark">
                  {{ especialidade.nome }}
                </span>
              </td>

              <td class="small text-muted">
                {{ especialidade.descricao || "—" }}
              </td>

              <td class="text-end px-4">
                <button
                  class="btn btn-sm btn-outline-secondary rounded-3 me-1 px-3"
                  @click="abrirModal(especialidade)"
                >
                  <i class="bi bi-pencil"></i>
                </button>

                <button
                  class="btn btn-sm btn-outline-danger rounded-3 px-3"
                  @click="removerEspecialidade(especialidade)"
                >
                  <i class="bi bi-trash"></i>
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Modal -->
      <div
        v-if="modalAberto"
        class="modal-overlay d-flex align-items-center justify-content-center"
        @click.self="fecharModal"
      >
        <div class="modal-card p-4">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h5 class="fw-bold mb-0">
              {{
                editando
                  ? "Editar Especialidade"
                  : "Nova Especialidade"
              }}
            </h5>

            <button
              class="btn btn-sm btn-outline-secondary rounded-circle"
              @click="fecharModal"
            >
              <i class="bi bi-x"></i>
            </button>
          </div>

          <div class="row g-3">
            <div class="col-12">
              <label class="form-label">Nome *</label>

              <input
                v-model="formulario.nome"
                class="form-control rounded-3"
                placeholder="Ex: Cardiologia"
                required
              />
            </div>

            <div class="col-12">
              <label class="form-label">Descrição</label>

              <textarea
                v-model="formulario.descricao"
                class="form-control rounded-3"
                placeholder="Breve descrição da especialidade"
                rows="3"
              ></textarea>
            </div>
          </div>

          <div class="d-flex gap-2 mt-4">
            <button
              class="btn btn-danger flex-grow-1 rounded-3 fw-bold"
              @click="salvarEspecialidade"
              :disabled="salvando"
            >
              <span
                v-if="salvando"
                class="spinner-border spinner-border-sm me-2"
              ></span>

              {{
                salvando
                  ? "Salvando..."
                  : editando
                  ? "Salvar Alterações"
                  : "Cadastrar Especialidade"
              }}
            </button>

            <button
              class="btn btn-outline-secondary rounded-3 px-4"
              @click="fecharModal"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from "vue";
import SidebarAdminComp from "../../components/admin/SidebarAdminComp.vue";
import api from "../../services/api";

const especialidades = ref([]);
const carregando = ref(false);
const salvando = ref(false);
const erro = ref(null);

const modalAberto = ref(false);
const editando = ref(false);

const formulario = reactive({
  id: null,
  nome: "",
  descricao: "",
});

const endpoint = "/especialidades/";

// Buscar especialidades
async function buscarEspecialidades() {
  carregando.value = true;
  erro.value = null;

  try {
    const resposta = await api.get(endpoint);
    especialidades.value = resposta.data;
  } catch (err) {
    erro.value =
      err.response?.data?.message ||
      err.message ||
      "Erro ao carregar especialidades.";
  } finally {
    carregando.value = false;
  }
}

// Abrir modal
function abrirModal(especialidade = null) {
  erro.value = null;

  if (especialidade) {
    editando.value = true;

    formulario.id = especialidade.id;
    formulario.nome = especialidade.nome;
    formulario.descricao = especialidade.descricao;
  } else {
    editando.value = false;
    limparFormulario();
  }

  modalAberto.value = true;
}

// Fechar modal
function fecharModal() {
  modalAberto.value = false;
  limparFormulario();
}

// Limpar formulário
function limparFormulario() {
  formulario.id = null;
  formulario.nome = "";
  formulario.descricao = "";
}

// Salvar especialidade
async function salvarEspecialidade() {
  if (!formulario.nome.trim()) {
    erro.value = "O campo Nome é obrigatório.";
    return;
  }

  salvando.value = true;
  erro.value = null;

  try {
    const payload = {
      nome: formulario.nome,
      descricao: formulario.descricao,
    };

    if (editando.value) {
      await api.put(`${endpoint}/${formulario.id}`, payload);
    } else {
      await api.post(endpoint, payload);
    }

    fecharModal();
    await buscarEspecialidades();
  } catch (err) {
    erro.value =
      err.response?.data?.message ||
      err.message ||
      "Erro ao salvar a especialidade.";
  } finally {
    salvando.value = false;
  }
}

// Excluir especialidade
async function removerEspecialidade(especialidade) {
  if (
    !confirm(
      `Deseja excluir a especialidade "${especialidade.nome}"? Esta ação não poderá ser desfeita.`
    )
  ) {
    return;
  }

  try {
    await api.delete(`${endpoint}/${especialidade.id}`);
    await buscarEspecialidades();
  } catch (err) {
    erro.value =
      err.response?.data?.message ||
      err.message ||
      "Erro ao excluir a especialidade.";
  }
}

onMounted(buscarEspecialidades);
</script>

<style scoped>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css");

.dashboard-wrapper {
  background-color: #fff5f5;
  min-height: 100vh;
}

.section-card {
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.3rem;
  display: block;
}

.form-control {
  border: 1.5px solid #e2e8f0;
  padding: 10px 14px;
}

.form-control:focus {
  border-color: #dc2626;
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.1);
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  backdrop-filter: blur(2px);
}

.modal-card {
  background: white;
  border-radius: 20px;
  width: 100%;
  max-width: 540px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
  max-height: 90vh;
  overflow-y: auto;
}
</style>