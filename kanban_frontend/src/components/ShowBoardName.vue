<template>
  <div class='showboardname'>
    <router-link :to="{name: 'kanbanboard', params: {id: name.id } }">
      <div class='boardname'>{{ name.title }}</div>
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'show-board-name',
  props: ['name']
}

</script>

<style>

.showboardname {
  border-radius: 5px;
  height: 40px;
  width: 340px;
  background-color: rgb(126, 173, 163);
	padding-top: 10px;
	padding-left: 10px;
  margin-bottom: 10px;
}

.boardname {
  color: rgb(244, 206, 70);
	margin: auto 10px;
}

</style>
