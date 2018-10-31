<template>
  <kanban-board :stages="stages" :blocks="blocks" @update-block="updateBlock">
    <div v-for="block in blocks" :slot="block.id" :key="block.id">
      <div>
        <strong>id:</strong> {{ block.id }}
      </div>
      <div>
        {{ block.title }}
      </div>
    </div>
  </kanban-board>
</template>


<script>

export default {
  name: "KanbanBoard",
  data: function() {
    return {
      stages: ["on-hold", "in-progress", "needs-review", "approved"],
      blocks: this.getBlocks(),
      listPrimitive: null
    };
  },
  methods: {
    updateBlock: function(id, status) {
      let block = this.blocks[id];
      this.listPrimitive.update(id, { id, title: block.title, status });
    },

    getBlocks: function() {

      this.$http.get(`/app/api/cards/?board=${this.$route.id}`).then((response) => {
        this.blocks = response.data
      }).catch((response) => {
        console.log(response)
      })

      return this.blocks
    }
  },
};


</script>

<style lang='scss'>
@import "node_modules/vue-kanban/src/assets/kanban.scss";
</style>
