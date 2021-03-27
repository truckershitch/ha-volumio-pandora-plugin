# Set input_select options from a comma-delimited string
# See https://community.home-assistant.io/t/input-select-set-options-also-update-the-current-state-too-what-to-do/153340/11
# Modified 11/30/2020
# Cyber Monday Bitch!

entity_id = data.get('entity_id')
options = data.get('options')
# retain_state in data_template
# either 'hell yes' or 'hell no':
# True/False/Yes/No/Y/N evaluate to boolean
# we need type str! surround with quotes!
retain_state = data.get('retain_state', 'hell no')
retain_state = 'hell yes' in retain_state.lower()

google_sync_script_name = 'script.google_sync_devices'
google_sync_data = {'entity_id': google_sync_script_name}

if entity_id is not None and options is not None:
    options = [ o.strip() for o in options.split(",") ]

    if entity_id.startswith('input_select') and entity_id.count('.') == 1:
        set_options_data = {'entity_id': entity_id, 'options': options}
        hass.services.call('input_select', 'set_options', set_options_data)

        if retain_state:
            current_state = hass.states.get(entity_id)

            if current_state is not None and current_state.state in options:
                select_option_data = {'entity_id': entity_id, 'option': current_state.state}
                hass.services.call('input_select', 'select_option', select_option_data)

        hass.services.call('script', 'turn_on', google_sync_data) # sync Google devices to HA
