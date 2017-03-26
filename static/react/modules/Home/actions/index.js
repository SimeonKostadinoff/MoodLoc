/**
 * Created by boyanbonev on 26/03/2017.
 */

export function showLocationsResult(jsonResult) {
    return {
        type: "SHOW_LOCATIONS",
        locations: jsonResult
    };
}

export function changeSearch(search) {
    return {
        type: 'CHANGE_SEARCH',
        search
    };
}

export function changeSearchAndLoadLocations(search) {
    return (dispatch, getState) => {
        dispatch(changeSearch(search));
        dispatch(loadLocations());
    };
}

export function loadLocations() {
    return (dispatch, getState) => {
        let state = getState();
        let { search } = state.locations;

        let url = `http://127.0.0.1:8000/classify/?sentance=`;
        if(search) {
            url+=`${search}`
        } else {
            url+="Manchester"
        }

        $.get(url, data => {
            console.log("DATA: ", data);
            dispatch(showLocationsResult(data));
        });
        /*let data = [{
            lat: 53.690201 + parseInt(search),
            lng: -1.757813,
            search: search,
            percentage: 0.7,
            key: '0',
        },
        {
            lat: 54.690201 + parseInt(search),
            lng: -1.757813,
            search: search,
            percentage: 0.3,
            key: '1',
        }];*/
        //dispatch(showLocationsResult(data));
    }
}
