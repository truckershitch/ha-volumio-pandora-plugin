
@service
def update_options(entity_id, options_csv, retain_state='hell no'):
    retain_state = 'hell yes' in retain_state.lower()
    if entity_id is not None and options_csv is not None:
        options = [ o.strip() for o in options_csv.split(",") ]

        if entity_id.startswith('input_select') and entity_id.count('.') == 1:
            input_select.set_options(entity_id=entity_id, options=options)

            if retain_state:
                current_state = entity_id

                if current_state is not None and current_state in options:
                    input_select.select_option(entity_id=entity_id, option=current_state)
                    
    script.google_sync_devices()