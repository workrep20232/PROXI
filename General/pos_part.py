def pos_partition(i,M):
    # Generate a list of indices from 0 to number of edges
    indices = list(range(m))

    # Shuffle the indices randomly
    random.shuffle(indices)

    # Select 70% of the indices
    pos_train_ind = indices[:int(0.7 * len(indices))]

    # Select the remaining indices
    remaining_indices = indices[int(0.7 * len(indices)):]

    # Select 10% of the remaining indices
    pos_val_ind = remaining_indices[:int(1/3 * len(remaining_indices))]

    pos_test_ind = remaining_indices[int(1/3 * len(remaining_indices)):]

    # save the indices
    pos_train_ind = pd.DataFrame(pos_train_ind)
    pos_train_ind.to_csv('train_pos_index'+str(i)+'.csv')

    pos_val_ind = pd.DataFrame(pos_val_ind)
    pos_val_ind.to_csv('valid_pos_index'+str(i)+'.csv')

    pos_test_ind = pd.DataFrame(pos_test_ind)
    pos_test_ind.to_csv('test_pos_index'+str(i)+'.csv')

    return