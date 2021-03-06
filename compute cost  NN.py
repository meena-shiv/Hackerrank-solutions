def compute_cost(A2, Y, parameters):
    """
    Computes the cross-entropy cost given in equation (13)
    
    Arguments:
    A2 -- The sigmoid output of the second activation, of shape (1, number of examples)
    Y -- "true" labels vector of shape (1, number of examples)
    parameters -- python dictionary containing your parameters W1, b1, W2 and b2
    
    Returns:
    cost -- cross-entropy cost given equation (13)
    """
    
    m = Y.shape[1] # number of example

    # Compute the cross-entropy cost
    ### START CODE HERE ### (≈ 2 lines of code)
    
    #### WORKING SOLUTION 1: USING np.multiply & np.sum ####
    #logprobs = np.multiply(Y ,np.log(A2)) + np.multiply((1-Y), np.log(1-A2))
    #cost = (-1/m) * np.sum(logprobs)
    
    #### WORKING SOLUTION 2: USING np.dot ####
    cost = np.float64((-1.0/m) * (np.dot(Y, np.log(A2).T) + np.dot(1-Y, np.log(1-A2).T)))
    
    ### END CODE HERE ###
    
    cost = np.squeeze(cost)     # makes sure cost is the dimension we expect. 
                                # E.g., turns [[17]] into 17 
    cost = cost.astype(float)
    assert(isinstance(cost, float))
    
    return cost


A2, Y_assess, parameters = compute_cost_test_case()

print("cost = " + str(compute_cost(A2, Y_assess, parameters)))
