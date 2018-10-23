<template>
  <div id="listofboards">
    <show-board-name
        v-for="kanbanBoard in kanbanBoardsList"
        v-bind:key="kanbanBoard.id"
        v-bind:name="kanbanBoard"></show-board-name>
    <div class='showboardname'>
        <div v-on:click="OpenModal()" class='boardname'>Create</div>
    </div>
  </div>

</template>

<script>
import ShowBoardName from './ShowBoardName'

export default {
  name: 'Boards',

  components: {
    ShowBoardName,
  },

  data: function() {

    return {
      kanbanBoardsList: this.getKanbanBoardsList(),
      boardTitle: '',
      ownerName: ''
    }
  },

  methods: {

    getKanbanBoardsList: function() {

      // function sets list of kanban boards

      this.$http.get('/app/api/kanbanboards/').then((response) => {
        this.kanbanBoardsList = response.data
      }).catch((response) => {
        console.log(response)
      })

      return this.kanbanBoardsList
    },

    OpenModal: function() {
      this.$modal.show({
        template: `<div class='modal-form'>
                      <div class='modal-input'>
                          <input type='text' placeholder="title" v-model="boardTitle">
                      </div>
                      <div class='modal-input'>
                          <input type='text' placeholder="owner" v-model="ownerName">
                      </div>
                      <button @click="$emit('close')">Close</button>
                  </div>`,
        props: [],
      }, {/* data for props */}, {
        // sizes of modal window
        width: 300,
        height: 200,
      }, {
        // funcitons for events
        'before-open': this.beforeOpen,
        'before-close': this.beforeClose
      })
    },

    beforeOpen: function(event) {
      console.log(event)
      console.log(this.data)
    },

    beforeClose: function(event) {
      console.log(event)
      console.log(this.data)
    },

    beforeMount: function() {
      this.getKanbanBoardsList()
    },

  },

}

</script>

<style>

.modal-form {
  width: 250px;
  height: 80px;
  margin: auto;
  margin-top: 50px;
}

.modal-input {
  width: 250px;
  height: 30px;
  margin-bottom: 10px;
}

</style>
