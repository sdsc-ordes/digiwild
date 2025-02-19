from validation_submission.utils_individual import add_data_to_individual

def save_details(tag, data, individual):
                individual = add_data_to_individual(tag, data, individual)
                return individual

def save_image(camera, individual):
            individual = add_data_to_individual("image", camera.tolist(), individual)
            return individual