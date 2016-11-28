var request = require('superagent');
var React = require('react');
var ReactDOM = require('react-dom');
import update from 'immutability-helper';
import styles from '../css/base.css';


var Comment = React.createClass ({

    getInitialState: function() {
        return {
            editing: false,
            value: "",
        }
    },


    edit: function(){
        this.setState({editing: true})
    },


    remove: function(){
        var delUrl = 'http://127.0.0.1:8000/noteapp/note/' + (this.props.index) + '/';
        request.del(delUrl).send(this.props.index).then((response) => {
            this.props.deleteFromBoard(this.props.arr_id)

        });
    },


    save: function(){
        this.setState({editing: false})
        var putUrl = 'http://127.0.0.1:8000/noteapp/note/' + (this.props.index) + '/';

        request.put(putUrl).send({id : this.refs.newText.value, text : this.refs.newText.value}).then((response) => {

            this.props.updateCommentText(response.body, this.props.arr_id)
        });
        console.log('Updated note')
    },


//    handleChange: function() {
////        this.props({value: event.target.value});
//    },


      renderNormal: function() {

        return (
        <div>

                <textarea value={this.props.children} readOnly></textarea>
                <button onClick={this.edit}>Edit</button>
                <button onClick={this.remove}>Remove</button>

        </div>
        )
     },


    renderForm: function() {
        return (
           <div>
                <textarea ref='newText' value={this.refs.value} ></textarea>
                <button onClick={this.save}>Save</button>
           </div>
        )
    },


    render: function() {
            if(this.state.editing){
                return this.renderForm();
            }else{
                return this.renderNormal();
            }
    }
})

var Board = React.createClass({

        getInitialState: function() {
            return{
                comments: [],
            }
        },

//        gets all the notes from db
        getUpdate: function(){
            console.log('UPDATE from DB')
           var url = 'http://127.0.0.1:8000/noteapp/note/';
            request.get(url).then((response) => {
                this.setState({
                    comments: response.body
               });
            });
        },


        componentDidMount: function(){
            console.log('did MOUNT')
            var url = 'http://127.0.0.1:8000/noteapp/note/';
            request.get(url).then((response) => {
                this.setState({
                    comments: response.body,
               });
            });
        },


//        adds a new note box, and saves that note to the db, and calls an update function
        add: function (add_text){
            var postUrl = 'http://127.0.0.1:8000/noteapp/note/';
            var arr = this.state.comments;
            arr.push({text: add_text})
            request.post(postUrl).send({text : add_text}).then((response) => {
                this.getUpdate()

         });
        },


//        removes comments
        removeComment: function(i) {
            var arr = this.state.comments
            arr.splice(i, 1);
            this.setState({comments: arr})
        },


        updateComment: function(comment, i) {
            var arr = this.state.comments
            arr[i] = comment;
            this.setState({comments: arr})

        },


        eachComment: function (comment, i){
            return(
            <Comment key={i}  arr_id={i} index={comment.id} updateCommentText={this.updateComment} addComment={this.addComment}
                                deleteFromBoard={this.removeComment}>
                {comment.text}
            </Comment>
            );
        },


        render: function(){

            return(
                <div className={styles.box}>

                    <button onClick={this.add.bind(null, 'add new')}>Add New</button>
                    <div>
                          {this.state.comments.map(this.eachComment)}
                    </div>
                </div>
            );
        },
});


ReactDOM.render(

    <div>
        <Board />

    </div>

    , document.getElementById('container'))
