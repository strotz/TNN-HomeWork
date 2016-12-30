function ret = cd1(rbm_w, visible_data)
% <rbm_w> is a matrix of size <number of hidden units> by <number of visible units>
% <visible_data> is a (possibly but not necessarily binary) matrix of size <number of visible units> by <number of data cases>
% The returned value is the gradient approximation produced by CD-1. It's of the same shape as <rbm_w>.
    
    visible_state = sample_bernoulli(visible_data);
    
    hidden_probability_1 = visible_state_to_hidden_probabilities(rbm_w, visible_state);
    hidden_state_1 = sample_bernoulli(hidden_probability_1);
    
    visible_probability_1 = hidden_state_to_visible_probabilities(rbm_w, hidden_state_1);
    visible_state_1 = sample_bernoulli(visible_probability_1);

    hidden_probability_last = visible_state_to_hidden_probabilities(rbm_w, visible_state_1);
    % hidden_state_last = sample_bernoulli(hidden_probability_last);

    d_G_by_rbm_w = configuration_goodness_gradient(visible_state, hidden_state_1) - configuration_goodness_gradient(visible_state_1, hidden_probability_last);
    % G = configuration_goodness(rbm_w, visible_state_1, hidden_state_last);
    ret = d_G_by_rbm_w; % rbm_w, visible_data;
end
