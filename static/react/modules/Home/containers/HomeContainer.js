/**
 * Created by boyanbonev on 26/03/2017.
 */
import React, {Component}  from 'react';
import { connect } from 'react-redux';
import { loadLocations, changeSearchAndLoadLocations } from '../actions';
import { bindActionCreators } from 'redux';

import MapComponent from '../components/MapComponent';
import SearchComponent from '../components/SearchComponent';

class HomeContainer extends Component {
    componentWillMount() {
        const { loadLocations } = this.props;
        loadLocations();
    }

    render() {
        const { rows, count, search } = this.props.locations;
        const { loadLocations, changeSearchAndLoadLocations  } = this.props;

        const divStyle = {
            width: '100%',
            height: '780px'
        };

        const onSearchChanged = query => changeSearchAndLoadLocations(query);

        return (
            <div>
                <SearchComponent search={search} onSearchChanged={onSearchChanged} />
                <div style={divStyle}>
                    <MapComponent data={rows}/>
                </div>
            </div>
        );
    }
}

const mapStateToProps = state => ({
    locations: state.locations,
});

const mapDispatchToProps = dispatch => bindActionCreators({
    loadLocations, changeSearchAndLoadLocations
}, dispatch);

export default connect(mapStateToProps, mapDispatchToProps)(HomeContainer);