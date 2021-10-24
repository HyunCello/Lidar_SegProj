#include <chrono>
#include <ctime>
#include <map>
#include <opencv/cv.h>
#include <string>
#include <unordered_map>
#include <vector>

#include "communication/abstract_client.h"
#include "communication/abstract_sender.h"
#include "utils/cloud.h"
#include "utils/radians.h"
#include "utils/timer.h"
#include "utils/useful_typedefs.h"

#include "clusterers/abstract_clusterer.h"
#include "clusterers/image_based_clusterer.h"
#include "image_labelers/diff_helpers/diff_factory.h"
#include "image_labelers/linear_image_labeler.h"
#include "projections/cloud_projection.h"

void Measure_save(uint64_t time_measure_1);

// YH