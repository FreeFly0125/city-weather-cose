import { createStore } from 'vuex';
import { state } from './states';
import { actions } from './actions';
import { mutations } from "./mutations"

export default createStore({
    state,
    actions,
    mutations,
});
