
"use strict";

let save_3d_map = require('./save_3d_map.js')
let stop_3d_mapping = require('./stop_3d_mapping.js')
let start_3d_mapping = require('./start_3d_mapping.js')
let stop_remote_stream = require('./stop_remote_stream.js')
let toggle_led = require('./toggle_led.js')
let set_led_status = require('./set_led_status.js')
let set_pose = require('./set_pose.js')
let start_remote_stream = require('./start_remote_stream.js')
let reset_odometry = require('./reset_odometry.js')
let start_object_detection = require('./start_object_detection.js')
let stop_svo_recording = require('./stop_svo_recording.js')
let reset_tracking = require('./reset_tracking.js')
let stop_object_detection = require('./stop_object_detection.js')
let start_svo_recording = require('./start_svo_recording.js')
let save_area_memory = require('./save_area_memory.js')

module.exports = {
  save_3d_map: save_3d_map,
  stop_3d_mapping: stop_3d_mapping,
  start_3d_mapping: start_3d_mapping,
  stop_remote_stream: stop_remote_stream,
  toggle_led: toggle_led,
  set_led_status: set_led_status,
  set_pose: set_pose,
  start_remote_stream: start_remote_stream,
  reset_odometry: reset_odometry,
  start_object_detection: start_object_detection,
  stop_svo_recording: stop_svo_recording,
  reset_tracking: reset_tracking,
  stop_object_detection: stop_object_detection,
  start_svo_recording: start_svo_recording,
  save_area_memory: save_area_memory,
};
