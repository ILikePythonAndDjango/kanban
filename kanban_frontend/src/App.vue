<template>
<div class="wrapper">
  <div id="app">
    <div id="listofboards" v-if="kanbanBoardsList.length && showKanbanBoardsList">
      <show-board-name
          v-for="kanbanBoard of kanbanBoardsList"
          v-bind:key="kanbanBoard.id"
          v-bind:name="kanbanBoard.title"
          v-on:click="showKanbanBoard(kanbanBoard.id)"></show-board-name>
    </div>

    <div v-if="!showKanbanBoardsList" v-on:click="showKanbanBoardsList=true" class="buttonkanban">
      <!-- This block is shown if you see kanban board -->
      <router-view/>
    </div>
  </div>
</div>
</template>

<script>

/* eslint-disable */

import ShowBoardName from '@/components/ShowBoardName'

export default {
  name: 'App',

  components: {
    ShowBoardName,
  },

  data() {
    return {

      kanbanBoardsList: [],
      kanbanBoardDetail: null,

      // boolean flag that indicate status of list of kanban boards
      showKanbanBoardsList: false,

      // shouldn't set this vaibale
      _showKanbanBoardDetail: !this.showKanbanBoardsList
    }
  },

  methods: {

    handleError: function(error_response) {
      alert(error_response)
    },

    getKanbanBoardsList: function() {

      // function returns and sets list of kanban boards

      this.$http.get('/app/api/kanbanboards/').then((response) => {
        this.kanbanBoardsList = response.data
      }).catch((response) => {
        this.handleError(response)
      })

      return this.kanbanBoardsList
    },

    getKanbanBoardDetail: function(id) {

      // function returns and sets details of kanban board that has this id

      this.$http.get(`/app/api/kanbanboards/${id}/`).then((response) => {
        this.kanbanBoard = response.data
        this.handleError(this.kanbanBoard)
      }).catch((response) => {
        this.handleError(response)
      })

      return this.kanbanBoardDetail
    },

    showKanbanBoardDetail: function(id) {

      // function show details of kanban board that has this id

      var kanbanBoard = this.getKanbanBoardDetail(id)
      this.showKanbanBoardsList = false
    }
  },

  beforeMount(){
    this.getKanbanBoardsList()
    this.showKanbanBoardsList = true
 },
}
</script>

<style>

/* CSS Reset */

html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0px;
	padding: 0px;
	border: 0px;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}

/* CSS Reset */

.wrapper {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: rgb(25, 26, 29);
}

#main {
  position: relative;
  min-width: 720px;
  max-width: 960px;
  height: 100%;
  margin: 0px auto;
}

#listofboards {
  width: 360px;
  min-height: 720px;
  max-height: 960px;
  margin: 0px auto;
  padding: 10px;
}

.showboardname {
  border-radius: 5px;
  height: 40px;
  width: 340px;
  background-color: rgb(126, 173, 163);
	padding-top: 10px;
	padding-left: 10px;
}

.boardname {
  color: rgb(244, 206, 70);
	margin: auto 10px;
}
</style>
