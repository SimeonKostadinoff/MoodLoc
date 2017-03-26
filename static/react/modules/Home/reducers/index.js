/**
 * Created by boyanbonev on 26/03/2017.
 */

function getParameterByName(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.hash);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
};

const LOCATIONS_INITIAL = {
    rows: [],
    count: 0,
    page: 1,
    search: getParameterByName('search'),
    locations: {},
};

export const locations = (state=LOCATIONS_INITIAL, action) => {
    switch (action.type) {
        case 'SHOW_LOCATIONS':
            return Object.assign({}, state, {
                rows: action.locations,
                count: action.locations.length,
            });
        case 'CHANGE_SEARCH':
            return Object.assign({}, state, {
                search: action.search
            });
        default:
            return state;
    }
};