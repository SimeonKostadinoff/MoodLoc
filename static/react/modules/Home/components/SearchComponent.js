/**
 * Created by boyanbonev on 26/03/2017.
 */
import React from 'react';
import ReactDOM from 'react-dom';


export default class SearchPanel extends React.Component {
    constructor() {
        super()
        this.onSearchChange = this.onSearchChange.bind(this)
        this.onClearSearch = this.onClearSearch.bind(this)
        this.state = {}
    }

    render() {
        const textBoxStyle = {
            height: '4em',
            'padding-top': '2em',
            opacity: '0.5',
            background: 'black',
            'border-top': '3px solid #ccc',
            'border-bottom': '3px solid #ccc',
            'margin-top': '5.0em',
        };

        const onTop = {
            position: 'relative',
            top: '4.7em',
        };

        return (
            <div>
                <div>
                    <input ref='search' name='searchTerm' type='text' defaultValue={this.props.search} value={this.state.search} onChange={this.onSearchChange } />
                    <button value="" onClick={this.onSearchChange}>
                    </button>
                </div>
            </div>
        )
    }

    onSearchChange() {
        let query = ReactDOM.findDOMNode(this.refs.search).value;
        if (this.promise) {
            clearInterval(this.promise)
        }
        this.setState({
            search: query
        });
        this.promise = setTimeout(() => this.props.onSearchChanged(query), 1000);
    }

    onClearSearch() {
        this.setState({
            search: ''
        });
        this.props.onSearchChanged(undefined)

    }
}