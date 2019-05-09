import collections
class LRU_Cache:

    def __init__(self, space, timeout):
        #1 - Simplicity. Integration needs to be dead simple.
        # implement the LRU cache with just one signle ordered dictionary 
        self.queue = collections.OrderedDict()
        self.space = space
        self.timeout = timeout
        #3 - Near real time replication of data across Geolocation. Writes need to be in real time.
        #4 - Data consistency across regions
        #5 - Locality of reference, data should almost always be available from the closest region
        self.lock = False
        
    def time_tick(self):
        # time tick +1 to all element every time the class is bing access
        rem_list=[]
        for key in self.queue:
            # 7 Cache can expire after a few ticks
            if self.queue[key][1]>=self.timeout:
                rem_list.append(key) 
            else:    
                self.queue[key][1]+=1
        
        for key in rem_list:
            self.queue.pop(key) 
        

    def get(self, key):
        #2 - Resilient to network failures or crashes.
        try:
            self.time_tick()

            if key not in self.queue:
                return 'key '+str(key)+' is not in the cache'
            res = self.queue.pop(key) 
            self.queue[key] = res    # set key as the newest one
            #print(len(self.queue))

            return res[0]
        except:
            code="-1"
            print("get request failed with code ",code)


    def set(self, key, value):
        #4 - Data consistency across regions: adding a lock to prevent from dirty write 
        if self.lock ==False:
            self.lock =True
        #2 - Resilient to network failures or crashes.
            try:
                self.time_tick()
                if key in self.queue:   
                    self.queue.pop(key)
                elif self.space > 0:
                    self.space -= 1  
                else: 
                    # 6. flexiable schema design: pop the item to make the cache flexiable in space
                    self.queue.popitem(last=False) 
                # 7 initialize cache time with 0
                self.queue[key] = [value,0]
                #print(self.queue[key])
            except:
                code="-1"
                print("set request failed with code ",code)
            self.lock =False

cache = LRU_Cache(5,6)
#print(cache.get(1))
cache.set(1,1)


cache.set(2,2)
cache.set(3,3)
cache.set(4,4)
cache.set(5,5)

print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
print(cache.get(4))
print(cache.get(5))
