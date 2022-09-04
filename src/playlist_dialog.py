# Copyright (C) 2019-2021 Unrud <unrud@outlook.com>
#
# This file is part of Video Downloader.
#
# Video Downloader is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Video Downloader is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Video Downloader.  If not, see <http://www.gnu.org/licenses/>.

import gettext

from gi.repository import GObject, Gtk

from video_downloader.util import ConnectionManager, gobject_log

N_ = gettext.gettext


class PlaylistDialog(Gtk.MessageDialog):
    def __init__(self, parent):
        super().__init__(modal=True, destroy_with_parent=True,
                         message_type=Gtk.MessageType.QUESTION,
                         text='<b>%s</b>' % GObject.markup_escape_text(
                             N_('Download Playlist?')), use_markup=True,
                         secondary_text=N_('The video is part of a playlist.'))
        gobject_log(self)
        self._cm = ConnectionManager()
        self.set_transient_for(parent)
        self.add_button(N_('Single Video'), Gtk.ResponseType.NO)
        self.add_button(N_('All Videos in Playlist'), Gtk.ResponseType.YES)
        self.set_default_response(Gtk.ResponseType.NO)

    def destroy(self):
        self._cm.disconnect()
        super().destroy()
