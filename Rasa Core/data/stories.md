## happy path
* greet
  - utter_greet

## thanks path
* thanks
  - utter_welcome

## how you doing path
* howdoing
  - utter_respond

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## reboot affirm path
* reboot{"device":"MRI_scanner"}
  - utter_reboot

## power off affirm path
* power_off{"device":"MRI_scanner"}
  - utter_power_off
  - utter_did_that_help
* affirm
  - utter_happy

## power off deny path
* power_off{"device":"MRI_scanner"}
  - utter_power_off
  - utter_did_that_help
* deny
  - utter_canthelp

## power on affirm path
* power_on{"device":"MRI_scanner"}
  - utter_power_off
  - utter_did_that_help
* affirm
  - utter_happy

## power on deny path
* power_on{"device":"MRI_scanner"}
  - utter_power_off
  - utter_did_that_help
* deny
  - utter_canthelp

## log error affirm path
* log_error{"logerror":"log","device":"MRI_scanner"}
  - utter_log_error
  - utter_did_that_help
* affirm
  - utter_happy

## log error deny path
* log_error{"logerror":"log","device":"MRI_scanner"}
  - utter_log_error
  - utter_did_that_help
* deny
  - utter_canthelp

## restart coldhead affirm path
* restart_coldhead{"cooling":"coldhead","device":"MRI_scanner"}
  - utter_restart_coldhead
  - utter_did_that_help
* affirm
  - utter_happy

## restart coldhead deny path
* restart_coldhead{"cooling":"coldhead","device":"MRI_scanner"}
  - utter_restart_coldhead
  - utter_did_that_help
* deny
  - utter_canthelp

## reboot chiller affirm path 
* reboot_chiller{"cooling":"chiller","device":"MRI_scanner"}
  - utter_reboot_chiller
  - utter_did_that_help
* affirm
  - utter_happy

## reboot chiller deny path 
* reboot_chiller{"cooling":"chiller","device":"MRI_scanner"}
  - utter_reboot_chiller
  - utter_did_that_help
* deny
  - utter_canthelp

## cleanup affirm path
* cleanup{"device":"MRI_scanner"}
  - utter_cleanup
  - utter_did_that_help
* affirm
  - utter_happy

## cleanup deny path
* cleanup{"device":"MRI_scanner"}
  - utter_cleanup
  - utter_did_that_help
* deny
  - utter_canthelp

## squeezeball affirm path
* squeeze_ball{"alarmbell":"alarm"}
  - utter_squeeze_ball
  - utter_did_that_help
* affirm
  - utter_happy

## squeezeball deny path
* squeeze_ball{"alarmbell":"alarm"}
  - utter_squeeze_ball
  - utter_did_that_help
* deny
  - utter_canthelp

## warm up affirm path
* warm_up{"warmup":"warmup","device":"MRI_scanner"}
  - utter_warm_up
  - utter_did_that_help
* affirm
  - utter_happy

## warm up deny path
* warm_up{"warmup":"warmup","device":"MRI_scanner"}
  - utter_warm_up
  - utter_did_that_help
* deny
  - utter_canthelp

## setup phantom affirm path
* setup_phantom{"imaging":"phantom","warmup":"warm"}
  - utter_setup_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## setup phantom deny path
* setup_phantom{"imaging":"phantom","warmup":"warm"}
  - utter_setup_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## register phantom affirm path
* register_phantom{"imaging":"phantom","quality":"QA"}
  - utter_register_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## register phantom deny path
* register_phantom{"imaging":"phantom","quality":"QA"}
  - utter_register_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## run warmup scan affirm path
* run_warmup_scan{"warmup":"warm","imaging":"phantom"}
  - utter_run_warmup_scan
  - utter_did_that_help
* affirm
  - utter_happy

## run warmup scan deny path
* run_warmup_scan{"warmup":"warm","imaging":"phantom"}
  - utter_run_warmup_scan
  - utter_did_that_help
* deny
  - utter_canthelp

## run phantom affirm path
* run_phantom{"imaging":"phantom","quality":"QA"}
  - utter_run_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## run phantom deny path
* run_phantom{"imaging":"phantom","quality":"QA"}
  - utter_run_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## run scans phantom affirm path
* run_scans_phantom{"imaging":"phantom","quality":"QA"}
  - utter_run_scans_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## run scans phantom deny path 
* run_scans_phantom{"imaging":"phantom","quality":"QA"}
  - utter_run_scans_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## runtime phantom affirm path
* runtime_phantom{"imaging":"phantom","quality":"QA"}
  - utter_runtime_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## runtime phantom deny path
* runtime_phantom{"imaging":"phantom","quality":"QA"}
  - utter_runtime_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## trigger test affirm path
* trigger_test{"stimuli_test":"test"}
  - utter_trigger_test
  - utter_did_that_help
* affirm
  - utter_happy

## trigger test deny path
* trigger_test{"stimuli_test":"test"}
  - utter_trigger_test
  - utter_did_that_help
* deny
  - utter_canthelp

## setup test phantom affirm path
* setup_test_phantom{"imaging":"phantom","stimuli_test":"test"}
  - utter_setup_test_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## setup test phantom deny path
* setup_test_phantom{"imaging":"phantom","stimuli_test":"test"}
  - utter_setup_test_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## register test phantom affirm path
* register_test_phantom{"imaging":"phantom","stimuli_test":"test"}
  - utter_register_test_phantom
  - utter_did_that_help
* affirm
  - utter_happy

## register test phantom deny path
* register_test_phantom{"imaging":"phantom","stimuli_test":"test"}
  - utter_register_test_phantom
  - utter_did_that_help
* deny
  - utter_canthelp

## runscans test affirm path
* runscans_test{"stimuli_test":"test"}
  - utter_runscans_test
  - utter_did_that_help
* affirm
  - utter_happy

## runscans test deny path
* runscans_test{"stimuli_test":"test"}
  - utter_runscans_test
  - utter_did_that_help
* deny
  - utter_canthelp

## coil warning resolve affirm path
* coil_warning_resolve{"message":"warning"}
  - utter_coil_warning_resolve
  - utter_did_that_help
* affirm
  - utter_happy

## coil warning resolve deny path
* coil_warning_resolve{"message":"warning"}
  - utter_coil_warning_resolve
  - utter_did_that_help
* deny
  - utter_canthelp

## coil warning reason affirm path
* coil_warning_reason{"message":"warning"}
  - utter_coil_warning_reason
  - utter_did_that_help
* affirm
  - utter_happy

## coil warning reason deny path 
* coil_warning_reason{"message":"warning"}
  - utter_coil_warning_reason
  - utter_did_that_help
* deny
  - utter_canthelp

## ant post warning message affirm path 
* ant_post_warning_message{"message":"warning"}
  - utter_ant_post_warning_message
  - utter_did_that_help
* affirm
  - utter_happy

## ant post warning message deny path 
* ant_post_warning_message{"message":"warning"}
  - utter_ant_post_warning_message
  - utter_did_that_help
* deny
  - utter_canthelp

## wrong coil warning affirm path 
* wrong_coil_warning{"message":"warning"}
  - utter_wrong_coil_warning
  - utter_did_that_help
* affirm
  - utter_happy

## wrong coil warning deny path
* wrong_coil_warning{"message":"warning"}
  - utter_wrong_coil_warning
  - utter_did_that_help
* deny
  - utter_canthelp

## adjustment measure abort affirm path 
* adjustment_measure_abort
  - utter_adjustment_measure_abort
  - utter_did_that_help
* affirm
  - utter_happy

## adjustment measure abort deny path 
* adjustment_measure_abort
  - utter_adjustment_measure_abort
  - utter_did_that_help
* deny
  - utter_canthelp

## gradient poweramp warning affirm path 
* gradient_poweramp_warning{"message":"warning"}
  - utter_gradient_poweramp_warning
  - utter_did_that_help
* affirm
  - utter_happy

## gradient poweramp warning deny path 
* gradient_poweramp_warning{"message":"warning"}
  - utter_gradient_poweramp_warning
  - utter_did_that_help
* deny
  - utter_canthelp

## registration error affirm path 
* registration_error
  - utter_registration_error
  - utter_did_that_help
* affirm
  - utter_happy

## registration error deny path 
* registration_error
  - utter_registration_error
  - utter_did_that_help
* deny
  - utter_canthelp

## trigger setup
* trigger_setup
  - utter_trigger_setup

## device selection affirm path 
* device_selection
  - utter_device_selection
  - utter_did_that_help
* affirm
  - utter_happy

## device selection deny path

* device_selection
  - utter_device_selection
  - utter_did_that_help
* deny
  - utter_canthelp

## response setting affirm path
* response_setting
  - utter_response_setting
  - utter_did_that_help
* affirm
  - utter_happy

## response setting deny path
* response_setting
  - utter_response_setting
  - utter_did_that_help
* deny
  - utter_canthelp

## troubleshooting path
* troubleshooting
  - utter_troubleshooting


## goggle Setup
* goggle_Setup
  - utter_goggle_Setup

## tech remote affirm path
* tech_remote{"task_box":"tech remote"}
  - utter_tech_remote
  - utter_did_that_help
* affirm
  - utter_happy

## tech remote deny path
* tech_remote{"task_box":"tech remote"}
  - utter_tech_remote
  - utter_did_that_help
* deny
  - utter_canthelp

## visuastim controller affirm path
* visuastim_controller
  - utter_visuastim_controller
  - utter_did_that_help
* affirm
  - utter_happy

## visuastim controller deny path
* visuastim_controller
  - utter_visuastim_controller
  - utter_did_that_help
* deny
  - utter_canthelp

## general troubleshoot affirm path
* general_troubleshooting
  - utter_general_troubleshooting
  - utter_did_that_help
* affirm
  - utter_happy

## genral troubleshoot deny path
* general_troubleshooting
  - utter_general_troubleshooting
  - utter_did_that_help
* deny
  - utter_canthelp

## troubleshoot google affirm path
* troubleshoot_google
  - utter_troubleshoot_goggle
  - utter_did_that_help
* affirm
  - utter_happy

## troubleshoot google deny path
* troubleshoot_google
  - utter_troubleshoot_goggle
  - utter_did_that_help
* deny
  - utter_canthelp

## resonance tech remote
* resonance_tech_remote{"task_box":"Tech remote"}
  - utter_resonance_tech_remote

## volume reset affirm path
* volume_reset{"tak_box":"tech remote"}
  - utter_volume_reset
  - utter_did_that_help
* affirm
  - utter_happy

## volume reset deny path
* volume_reset{"tak_box":"tech remote"}
  - utter_volume_reset
  - utter_did_that_help
* deny
  - utter_canthelp

## audio input affirm path
* audio_input{"task_box":"tech remote"}
  - utter_audio_input
  - utter_did_that_help
* affirm
  - utter_happy

## audio input deny path
* audio_input{"task_box":"tech remote"}
  - utter_audio_input
  - utter_did_that_help
* deny
  - utter_canthelp

## comm mode setting affirm path
* comm_mode_setting{"task_box":"tech remote"}
  - utter_comm_mode_setting
  - utter_did_that_help
* affirm
  - utter_happy

## comm mode setting deny path
* comm_mode_setting{"task_box":"tech remote"}
  - utter_comm_mode_setting
  - utter_did_that_help
* deny
  - utter_canthelp

## remote reset affirm path
* remote_reset{"task_box":"tech remote"}
  - utter_remote_reset
  - utter_did_that_help
* affirm
  - utter_happy

## remote reset deny path
* remote_reset{"task_box":"tech remote"}
  - utter_remote_reset
  - utter_did_that_help
* deny
  - utter_canthelp

## headphone
* headphone{"audio":"headphone"}
  - utter_headphone

## participant position affirm path
* participant_position{"audio":"headphone"}
  - utter_participant_position
  - utter_did_that_help
* affirm
  - utter_happy

## participant position deny path
* participant_position{"audio":"headphone"}
  - utter_participant_position
  - utter_did_that_help
* deny
  - utter_canthelp

## opto control affirm path
* opto_control
  - utter_opto_control
  - utter_did_that_help
* affirm
  - utter_happy

## opto control deny path
* opto_control
  - utter_opto_control
  - utter_did_that_help
* deny
  - utter_canthelp

## noise cancellation affirm path
* noise_cancellation
  - utter_noise_cancellation
  - utter_did_that_help
* affirm
  - utter_happy

## noise cancellation deny path
* noise_cancellation
  - utter_noise_cancellation
  - utter_did_that_help
* deny
  - utter_canthelp

## troubleshoot headphone affirm path
* troubleshoot_headphone{"audio":"headphone"}
  - utter_troubleshoot_headphone
  - utter_did_that_help
* affirm
  - utter_happy

## troubleshoot headphone deny path
* troubleshoot_headphone
  - utter_troubleshoot_headphone
  - utter_did_that_help
* deny
  - utter_canthelp

## HCP physio device setup affirm path
* HCP_physio_device_setup
  - utter_HCP_physio_device_setup
  - utter_did_that_help
* affirm
  - utter_happy

## HCP physio device setup deny path
* HCP_physio_device_setup
  - utter_HCP_physio_device_setup
  - utter_did_that_help
* deny
  - utter_canthelp

## firmm monitor affirm path 
* firmm_monitor
  - utter_firmm_monitor
  - utter_did_that_help
* affirm
  - utter_happy

## firmm monitor deny path 
* firmm_monitor
  - utter_firmm_monitor
  - utter_did_that_help
* deny
  - utter_canthelp

## mr camera affirm path
* mr_camera{"snapcam":"camera"}
  - utter_mr_camera
  - utter_did_that_help
* affirm
  - utter_happy

## mr camera deny path
* mr_camera{"snapcam":"camera"}
  - utter_mr_camera
  - utter_did_that_help
* deny
  - utter_canthelp

## camera equipments affirm path
* camera_equipments{"snapcam":"camera"}
  - utter_camera_equipments
  - utter_did_that_help
* affirm
  - utter_happy

## camera equipments deny path
* camera_equipments{"snapcam":"camera"}
  - utter_camera_equipments
  - utter_did_that_help
* deny
  - utter_canthelp

## setup camera affirm path
* setup_camera{"snapcam":"camera"}
  - utter_setup_camera
  - utter_did_that_help
* affirm
  - utter_happy

## setup camera deny path
* setup_camera{"snapcam":"camera"}
  - utter_setup_camera
  - utter_did_that_help
* deny
  - utter_canthelp

## Participant Setup camera affirm path
* Participant_Setup_camera{"snapcam":"camera"}
  - utter_Participant_Setup_camera
  - utter_did_that_help
* affirm
  - utter_happy

## Participant Setup camera deny path
* Participant_Setup_camera{"snapcam":"camera"}
  - utter_Participant_Setup_camera
  - utter_did_that_help
* deny
  - utter_canthelp

## cleanup camera affirm path
* cleanup_camera{"snapcam":"camera"}
  - utter_cleanup_camera
  - utter_did_that_help
* affirm
  - utter_happy

## cleanup camera affirm path
* cleanup_camera{"snapcam":"camera"}
  - utter_cleanup_camera
  - utter_did_that_help
* deny
  - utter_canthelp

## troubleshoot camera affirm path
* troubleshoot_camera{"snapcam":"camera"}
  - utter_troubleshoot_camera
  - utter_did_that_help
* affirm
  - utter_happy

## troubleshoot camera deny path
* troubleshoot_camera{"snapcam":"camera"}
  - utter_troubleshoot_camera
  - utter_did_that_help
* deny
  - utter_canthelp
