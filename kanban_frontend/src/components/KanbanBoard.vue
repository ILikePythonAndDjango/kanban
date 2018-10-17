<template>
  <div class="kanban">
    <div id="app">
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
    </div>
  </div>
</template>


<script>
import Vue from "vue";
import vueKanban from "vue-kanban";

Vue.use(vueKanban);

export default {
  name: "app",
  data() {
    return {
      stages: ["on-hold", "in-progress", "needs-review", "approved"],
      blocks: blocks,
      listPrimitive: null
    };
  },
  methods: {
    updateBlock(id, status) {
      let block = this.blocks[id];
      this.listPrimitive.update(id, { id, title: block.title, status });
    }
  },
};

const blocks = [
  {
    id: 0,
    status: "approved",
    title: "Buy coffee machine"
  },
  {
    id: 1,
    status: "in-progress",
    title: "Find better AirBnB options"
  },
  {
    id: 2,
    status: "on-hold",
    title: "Approve Q3 budget"
  },
  {
    id: 3,
    status: "approved",
    title: "Travel to Guaraguara"
  },
  {
    id: 4,
    status: "needs-review",
    title: "Add Redux to the app"
  },
  {
    id: 5,
    status: "approved",
    title: "Well, Sleep all day 👩‍🎤"
  },
  {
    id: 6,
    status: "in-progress",
    title: "Find language exchange partner"
  }
];

</script>

<style lang='scss'>
@import "node_modules/vue-kanban/src/assets/kanban.scss";
</style>
