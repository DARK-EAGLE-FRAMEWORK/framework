from tqdm import tqdm
# Ni Muhimu , to make everything loaded with time 

class bar_module2():

    loader = tqdm(total=5000, position=0, leave=False)
    for k in range(5000):
        loader.set_description('Loading Wait!!.....'.format(k))
        loader.update(1)
    loader.close()