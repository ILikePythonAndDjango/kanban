
Vue.component('show-board-name', {
  props: ['name'],
  template: "<div class='showboardname'><div class='boardname'>{{ name }}</div></div>",
})

var main = new Vue({
  el: '#main',

  data: {

    kanbanBoardsList: [],
    kanbanBoardDetail: null,

    // boolean flag that indicate status of list of kanban boards
    showKanbanBoardsList: false,

    // shouldn't set this vaibale
    _showKanbanBoardDetail: !this.showKanbanBoardsList
  },

  methods: {

    handleError: function(error_response) {
      alert(error_response)
    },

    getKanbanBoardsList: function() {

      // function returns and sets list of kanban boards

      this.$http.get('/api/kanbanboards/').then((response) => {
        this.kanbanBoardsList = response.data
      }).catch((response) => {
        this.handleError(response)
      })

      return this.kanbanBoardsList
    },

    getKanbanBoardDetail: function(id) {

      // function returns and sets details of kanban board that has this id

      this.$http.get(`/api/kanbanboards/${id}/`).then((response) => {
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
    this.getkanbanBoardsList()
    this.showKanbanBoardsList = true
 },

})
