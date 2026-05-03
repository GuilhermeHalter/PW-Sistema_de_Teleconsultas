<template>
  <div class="dashboard-wrapper d-flex">
    <!-- Sidebar -->
    <SidebarPatientComp />

    <!-- Conteúdo -->
    <main class="content flex-grow-1 p-4">
      <header class="mb-4">
        <h3 class="fw-bold text-dark mb-1">Meu Perfil</h3>
        <p class="text-muted">Gerencie suas informações pessoais e preferências</p>
      </header>

      <!-- Card Perfil Principal -->
      <div class="section-card p-4 mb-4 d-flex justify-content-between align-items-center">
        <div class="d-flex align-items-center gap-4">
          <div class="avatar-large">MS</div>
          <div>
            <h4 class="fw-bold text-dark mb-1">{{ user.nome }}</h4>
            <p class="text-muted mb-1">{{ user.email }}</p>
            <small class="text-secondary">Paciente desde Janeiro de 2025</small>
          </div>
        </div>
        <button class="btn btn-outline-custom">Alterar Foto</button>
      </div>

      <!-- Dados Pessoais -->
      <div class="section-card p-4 mb-4">
        <div class="d-flex align-items-center gap-2 mb-1">
          <i class="bi bi-person text-dark fs-5"></i>
          <h6 class="fw-bold mb-0">Dados Pessoais</h6>
        </div>
        <p class="text-muted small mb-4">Suas informações básicas de cadastro</p>

        <div class="row g-3">
          <div class="col-md-6">
            <label class="form-label">Nome Completo</label>
            <div class="input-container">
              <input v-model="user.nome" class="form-control-custom" />
            </div>
          </div>
          <div class="col-md-6">
            <label class="form-label">CPF</label>
            <div class="input-container">
              <input v-model="user.cpf" class="form-control-custom disabled-bg" disabled />
            </div>
          </div>
          <div class="col-md-6">
            <label class="form-label">E-mail</label>
            <div class="input-container">
              <i class="bi bi-envelope icon-input"></i>
              <input v-model="user.email" class="form-control-custom has-icon" />
            </div>
          </div>
          <div class="col-md-6">
            <label class="form-label">Telefone</label>
            <div class="input-container">
              <i class="bi bi-telephone icon-input"></i>
              <input v-model="user.telefone" class="form-control-custom has-icon" />
            </div>
          </div>
          <div class="col-md-6">
            <label class="form-label">Data de Nascimento</label>
            <div class="input-container">
              <input type="date" v-model="user.dataNascimento" class="form-control-custom" />
            </div>
          </div>
          <div class="col-md-6">
            <label class="form-label">Endereço</label>
            <div class="input-container">
              <i class="bi bi-geo-alt icon-input"></i>
              <input v-model="user.endereco" class="form-control-custom has-icon" />
            </div>
          </div>
        </div>
      </div>

      <!-- Histórico Médico -->
      <div class="section-card p-4 mb-4">
        <div class="d-flex align-items-center gap-2 mb-1">
          <i class="bi bi-shield-check text-dark fs-5"></i>
          <h6 class="fw-bold mb-0">Histórico Médico</h6>
        </div>
        <p class="text-muted small mb-3">Informações importantes para seus atendimentos</p>
        <label class="form-label fw-bold small mb-2">Alergias, medicamentos de uso contínuo, condições pré-existentes</label>
        <textarea
          v-model="user.historico"
          class="form-control-custom w-100"
          rows="3"
        ></textarea>
      </div>

      <!-- Preferências de Notificação -->
      <div class="section-card p-4 mb-4">
        <div class="d-flex align-items-center gap-2 mb-1">
          <i class="bi bi-bell text-dark fs-5"></i>
          <h6 class="fw-bold mb-0">Preferências de Notificação</h6>
        </div>
        <p class="text-muted small mb-4">Configure como deseja receber lembretes e alertas</p>

        <div class="d-flex flex-column gap-4">
          <div class="toggle-wrapper">
            <div class="toggle-text">
              <span class="fw-bold d-block">Notificações por E-mail</span>
              <small class="text-muted">Receber lembretes e confirmações por e-mail</small>
            </div>
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" v-model="user.emailNotif">
            </div>
          </div>

          <div class="toggle-wrapper">
            <div class="toggle-text">
              <span class="fw-bold d-block">Notificações por SMS</span>
              <small class="text-muted">Receber lembretes por mensagem de texto</small>
            </div>
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" v-model="user.smsNotif">
            </div>
          </div>

          <div class="toggle-wrapper">
            <div class="toggle-text">
              <span class="fw-bold d-block">Lembrete de Consulta</span>
              <small class="text-muted">Lembrete 24h e 1h antes da consulta</small>
            </div>
            <div class="form-check form-switch">
              <input class="form-check-input" type="checkbox" v-model="user.lembreteConsulta">
            </div>
          </div>
        </div>
      </div>

      <!-- Botão Salvar -->
      <div class="d-flex justify-content-end mb-5">
        <button class="btn btn-save d-flex align-items-center gap-2" @click="salvar">
          <i class="bi bi-save"></i> Salvar Alterações
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import SidebarPatientComp from "../components/patient/SidebarPatientComp.vue";

const user = reactive({
  nome: "Maria Silva",
  email: "maria.silva@email.com",
  cpf: "123.456.789-00",
  telefone: "(11) 99999-9999",
  dataNascimento: "1990-05-15",
  endereco: "Rua das Flores, 123 - São Paulo, SP",
  historico: "Alergia à penicilina. Uso contínuo de losartana.",
  emailNotif: true,
  smsNotif: true,
  lembreteConsulta: true,
});

const salvar = () => {
  console.log("Dados salvos:", user);
};
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
  background-color: #DFF2F0; /* Cor da paleta */
  color: #03A1E0; /* Azul claro da paleta */
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-size: 2rem;
}

/* Inputs e Forms */
.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #1e293b;
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
  transition: border-color 0.2s;
}

.form-control-custom:focus {
  outline: none;
  border-color: #03A1E0;
}

.form-control-custom.has-icon {
  padding-left: 40px;
}

.icon-input {
  position: absolute;
  left: 15px;
  color: #94a3b8;
  font-size: 1rem;
}

.disabled-bg {
  background-color: #f8fafc;
  cursor: not-allowed;
}

/* Toggles */
.toggle-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form-check-input {
  width: 3rem;
  height: 1.5rem;
  cursor: pointer;
}

.form-check-input:checked {
  background-color: #0468BF;
  border-color: #0468BF;
}

/* Botões */
.btn-outline-custom {
  border: 1px solid #cbd5e1;
  background: white;
  color: #475569;
  padding: 8px 16px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.btn-outline-custom:hover {
  background-color: #f8fafc;
  border-color: #94a3b8;
}

.btn-save {
  background-color: #0468BF; /* Azul principal da paleta */
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 12px;
  font-weight: 700;
  transition: background 0.3s;
}

.btn-save:hover {
  background-color: #0060B4;
}
</style>