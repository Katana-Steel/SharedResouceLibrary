/*
    2018 (c) Rene 'Katana Steel' Kjellerup, distributed under the terms of
    the GNU General Public Licenses version 3 or later for details see:
    http://www.gnu.org/licenses/gpl.html
*/
#include "dynres.h"
// minimal needed to access loadstring function
// and to verify the stored string table
void __attribute__((constructor)) InitializeResourceSystem() {
    setup_string_tables();
    setup_cursors();
    return;
}
