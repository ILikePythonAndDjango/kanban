<template>
  <div class='showboardname' v-on:click="showKanbanBoardDetail(key)"><div class='boardname'>{{ name }}</div></div>
</template>

<script>

export default {
  name: 'show-board-name',
  props: ['name']
}

</script>

<style>

</style>
