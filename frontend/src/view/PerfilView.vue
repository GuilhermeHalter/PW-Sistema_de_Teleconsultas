<template>
  <div class="dashboard-wrapper d-flex">
    <SidebarPatientComp />

    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Meu Perfil</h3>
        <p class="text-muted">Gerencie suas informações pessoais e preferências</p>
      </header>

      <div v-if="loading" class="text-center p-5">
        <div class="spinner-border text-primary-custom" role="status"></div>
        <p class="mt-2 text-muted">Carregando seus dados...</p>
      </div>

      <template v-else>
        <div class="section-card p-4 mb-4 d-flex justify-content-between align-items-center">
          <div class="d-flex align-items-center gap-4">
            <div class="avatar-large">{{ initials }}</div>
            <div>
              <h4 class="fw-bold text-dark mb-1">{{ user.nomeCompleto }}</h4>
              <p class="text-muted mb-1">{{ user.email }}</p>
              <small class="text-secondary">Paciente MedConnect</small>
            </div>
          </div>
          <button class="btn btn-outline-custom">Alterar Foto</button>
        </div>

        <div class="section-card p-4 mb-4">
          <div class="d-flex align-items-center gap-2 mb-1">
            <i class="bi bi-person text-dark fs-5"></i>
            <h6 class="fw-bold mb-0">Dados Pessoais</h6>
          </div>
          <p class="text-muted small mb-4">Suas informações básicas de cadastro</p>

          <div class="row g-3">
            <div class="col-md-6">
              <label class="form-label">Nome Completo</label>
              <input v-model="user.nomeCompleto" class="form-control-custom" placeholder="Ex: Maria Silva" />
            </div>
            <div class="col-md-6">
              <label class="form-label">CPF (Não alterável)</label>
              <input v-model="user.cpf" class="form-control-custom disabled-bg" disabled />
            </div>
            <div class="col-md-6">
              <label class="form-label">E-mail</label>
              <div class="input-container">
                <i class="bi bi-envelope icon-input"></i>
                <input v-model="user.email" class="form-control-custom has-icon" />
              </div>
            </div>
          </div>
        </div>

        <div class="section-card p-4 mb-4">
          <div class="d-flex align-items-center gap-2 mb-1">
            <i class="bi bi-shield-check text-dark fs-5"></i>
            <h6 class="fw-bold mb-0">Histórico Médico</h6>
          </div>
          <p class="text-muted small mb-3">Informações importantes para seus atendimentos</p>
          <textarea
            v-model="user.historico"
            class="form-control-custom w-100"
            rows="3"
            placeholder="Alergias, medicamentos de uso contínuo..."
          ></textarea>
        </div>

        <div class="d-flex justify-content-end mb-5">
          <button 
            class="btn btn-save d-flex align-items-center gap-2" 
            @click="handleSave"
            :disabled="saving"
          >
            <span v-if="saving" class="spinner-border spinner-border-sm"></span>
            <i v-else class="bi bi-save"></i>
            {{ saving ? 'Salvando...' : 'Salvar Alterações' }}
          </button>
        </div>
      </template>
    </main>
  </div>
</template>

<script setup>
import { reactive, onMounted, ref, computed } from "vue";
import SidebarPatientComp from "../components/patient/SidebarPatientComp.vue";
import { pacienteService } from "../services/paciente";

// Controle de UI
const loading = ref(true);
const saving = ref(false);

// Dados do Usuário
const user = reactive({
  nomeCompleto: "",
  email: "",
  cpf: "",
  telefone: "",
  dataNascimento: "",
  endereco: "",
  historico: "",
});

// Computada para Iniciais do Avatar
const initials = computed(() => {
  if (!user.nomeCompleto) return "??";
  const names = user.nomeCompleto.trim().split(" ");
  return names.length >= 2 
    ? (names[0][0] + names[names.length - 1][0]).toUpperCase()
    : names[0][0].toUpperCase();
});

// Busca dados iniciais
const fetchProfile = async () => {
  try {
    const data = await pacienteService.getMe();
    Object.assign(user, data);
  } catch (error) {
    console.error("Erro ao buscar perfil:", error);
  } finally {
    loading.value = false;
  }
};

// Salva alterações (PATCH)
const handleSave = async () => {
  saving.value = true;
  try {
    const response = await pacienteService.updateProfile(user);
    Object.assign(user, response);
    alert("Perfil atualizado com sucesso!");
  } catch (error) {
    alert("Erro ao salvar alterações. Verifique os dados.");
  } finally {
    saving.value = false;
  }
};

onMounted(fetchProfile);
</script>

<style scoped>
.dashboard-wrapper {
  background-color: #f4f9f9;
  min-height: 100vh;
}

.section-card {
  background: white;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
}

.avatar-large {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: #DFF2F0;
  color: #03A1E0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 2rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 0.5rem;
  display: block;
}

.input-container {
  position: relative;
  display: flex;
  align-items: center;
}

.form-control-custom {
  width: 100%;
  padding: 10px 15px;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  font-size: 0.9rem;
  color: #475569;
  transition: all 0.2s;
}

.form-control-custom:focus {
  outline: none;
  border-color: #03A1E0;
  box-shadow: 0 0 0 3px rgba(3, 161, 224, 0.1);
}

.form-control-custom.has-icon {
  padding-left: 40px;
}

.icon-input {
  position: absolute;
  left: 15px;
  color: #94a3b8;
}

.disabled-bg {
  background-color: #f8fafc;
  cursor: not-allowed;
}

.btn-outline-custom {
  border: 1px solid #cbd5e1;
  background: white;
  color: #475569;
  padding: 8px 16px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.85rem;
}

.btn-save {
  background-color: #0468BF;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 700;
  transition: opacity 0.2s;
}

.btn-save:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.text-primary-custom {
  color: #0468BF;
}
</style>