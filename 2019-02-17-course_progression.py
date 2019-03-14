# This problem was asked by Airbnb.

# We're given a hashmap associating each courseId key with a list of courseIds
# values, which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.

# Return null if there is no such ordering.

# For example, given
# {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
# should return ['CSC100', 'CSC200', 'CSCS300'].


def build_course_sequence(course_catalog):
    builder = PathBuilder(course_catalog)

    for course in course_catalog:
        result = builder.get_max_path_to(course)
        if len(result) == builder.num_courses():
            return result

    return None


class PathBuilder():
    def __init__(self, course_catalog):
        self.course_catalog = course_catalog

    def get_max_path_to(self, course):
        max_path = []
        for prereq in self.course_catalog[course]:
            path = self.get_max_path_to(prereq)
            if len(path) > len(max_path):
                max_path = path

        return max_path + [course]

    def num_courses(self):
        return len(self.course_catalog)


if __name__ == '__main__':
    CATALOG = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }

    print(build_course_sequence(CATALOG))


# Notes: Would have failed this one.  Second try is clean, but first wasn't
# good.  There are still possibly better ways to iterate through the catalog
# to guide the search, like ordering by num dependencies, but not sure if it's
# worth it.

# Analysis: Supplied solution is iterative, which makes the initial choices
# simple- courses with no prereqs.

# 1. Put all courses with no pre-requisites into our todo list.
# 2. For each course C in the todo list, find each course D which have C as a
# prerequisite and remove C from its list. Add D to the todo list.

# This is better than mine, certainly without caching of the recursion.
# Building the inverse map is only done once.  I probably should have done
# that here.
