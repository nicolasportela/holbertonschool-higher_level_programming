
$(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('UL.my_list > :last-child').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
