from custom_types import Problem
import numpy

def parse_input(f_in: str):
    """Parse the input file, fill and return the `Problem` class instance."""

    prob = Problem()

    with open(f_in, 'r') as f:
        conts = [[int(s) for s in i.rstrip().split()] for i in f.readlines()]

    # Remove last line if empty
    if conts[-1] == '':
        conts = conts[:-1]

    # Totals
    print(conts)
    prob.n_videos, prob.n_ends, prob.n_reqs, prob.n_caches, prob.cache_sizes = conts[0]

    # Video sizes
    prob.video_sizes = conts[1]

    # Latencies for all the endpoints to the datacenter + caches
    prob.datacenter_latencies = [0 for i in range(prob.n_ends)]
    prob.endpoint_cache_latencies = numpy.zeros((prob.n_ends, prob.n_caches), dtype=int)
    prob.endpoint_cache_latencies[:] = -1  # can't be reached

    cur_line = 2
    for end in range(prob.n_ends):
        prob.datacenter_latencies[end], prob.num_caches = conts[cur_line]
        cur_line += 1

        for cache in range(prob.num_caches):
            c = conts[cur_line]
            cur_line += 1
            prob.endpoint_cache_latencies[end, c[0]] = c[1]

    # Requests - 0 = no requests
    prob.endpoint_video_requests = numpy.zeros((prob.n_ends, prob.n_videos), dtype=int)
    for line in range(cur_line, len(conts)):
        v, e, r = conts[line]
        prob.endpoint_video_requests[e, v] = r

    # Print stuff
    print("# Videos: {} | # Endpoints: {} | # Requests: {} | # Caches: {} MB | # Cache Size: {}".format(prob.n_videos, prob.n_ends, prob.n_reqs, prob.n_caches, prob.cache_sizes))
    print("video_sizes: ", prob.video_sizes)
    print("datacenter_latencies: ", prob.datacenter_latencies)
    print("endpoint_cache_latencies:\n", prob.endpoint_cache_latencies)
    print("endpoint_video_requests:\n", prob.endpoint_video_requests)

    return prob
