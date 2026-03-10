<script setup></script>

<template>
  <h1>
    Sistema de Teleconsultas - Projeto de Programação Web
  </h1>
  <router-link to="/cadastro">Ir para Cadastro</router-link> <br/>
  <router-link to="/login">Ir para Login</router-link><br/>
  <router-link to="/home">Ir para Home</router-link><br/>
  <router-link to="/perfil">Ir para Perfil</router-link><br/>
  <router-link to="/gerenciar-agenda">Ir para Gerenciar Agenda</router-link><br/>
  <router-link to="/sala-teleconsulta">Ir para Sala Teleconsulta</router-link><br/>
  <router-link to="/pagamento">Ir para Pagamento</router-link><br/>
  <router-link to="/dashboard-paciente">Ir para Dashboard Paciente</router-link><br/>
  <router-link to="/historico-consultas">Ir para Histórico de Consultas</router-link><br/>
  <router-link to="/dashboard-medico">Ir para Dashboard Médico</router-link><br/>
  <router-link to="/lista-consultas">Ir para Lista de Consultas</router-link><br/>

  <router-view></router-view>
</template>

<style scoped></style>
