<?php
// Define the Reservation post type
function create_reservation_post_type() {
  register_post_type( 'reservation',
    array(
      'labels' => array(
        'name' => __( 'Reservations' ),
        'singular_name' => __( 'Reservation' )
      ),
      'public' => true,
      'has_archive' => true,
      'rewrite' => array('slug' => 'reservation'),
      'supports' => array( 'title', 'editor', 'custom-fields' ),
      'menu_icon' => 'dashicons-calendar-alt'
    )
  );
}
add_action( 'init', 'create_reservation_post_type' );

// Define the Reservation custom fields
function reservation_custom_fields() {
  add_meta_box( 'reservation_meta', __( 'Reservation Details' ), 'reservation_meta_callback', 'reservation' );
}
add_action( 'add_meta_boxes', 'reservation_custom_fields' );

function reservation_meta_callback( $post ) {
  wp_nonce_field( basename( __FILE__ ), 'reservation_nonce' );
  $reservation_date = get_post_meta( $post->ID, 'reservation_date', true );
  $reservation_time = get_post_meta( $post->ID, 'reservation_time', true );
  $reservation_party_size = get_post_meta( $post->ID, 'reservation_party_size', true );
  ?>
  <p>
    <label for="reservation_date"><?php _e( 'Reservation Date:' ); ?></label>
    <input type="text" name="reservation_date" id="reservation_date" value="<?php echo $reservation_date; ?>" />
  </p>
  <p>
    <label for="reservation_time"><?php _e( 'Reservation Time:' ); ?></label>
    <input type="text" name="reservation_time" id="reservation_time" value="<?php echo $reservation_time; ?>" />
  </p>
  <p>
    <label for="reservation_party_size"><?php _e( 'Party Size:' ); ?></label>
    <input type="number" name="reservation_party_size" id="reservation_party_size" value="<?php echo $reservation_party_size; ?>" />
  </p>
  <?php
}

function save_reservation_meta( $post_id ) {
  if ( !isset( $_POST['reservation_nonce'] ) || !wp_verify_nonce( $_POST['reservation_nonce'], basename( __FILE__ ) ) ) {
    return $post_id;
  }
  $reservation_date = sanitize_text_field( $_POST['reservation_date'] );
  $reservation_time = sanitize_text_field( $_POST['reservation_time'] );
  $reservation_party_size = sanitize_text_field( $_POST['reservation_party_size'] );
  update_post_meta( $post_id, 'reservation_date', $reservation_date );
  update_post_meta( $post_id, 'reservation_time', $reservation_time );
  update_post_meta( $post_id, 'reservation_party_size', $reservation_party_size );
}
add_action( 'save_post', 'save_reservation_meta' );
